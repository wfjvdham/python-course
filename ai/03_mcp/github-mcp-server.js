#!/usr/bin/env node
// Minimalistisch voorbeeld van een (sterk vereenvoudigde) MCP-achtige server voor GitHub.
// LET OP: Dit is NIET een volledige implementatie van het echte Model Context Protocol.
// Het demonstreert slechts basisconcepten: capabilities aankondigen, eenvoudige requests afhandelen.

import { Octokit } from 'octokit';
import process from 'node:process';

const octo = new Octokit({ auth: process.env.GITHUB_TOKEN });

// Eenvoudige helper om JSON-RPC berichten naar stdout te schrijven
function send(msg) {
  process.stdout.write(JSON.stringify(msg) + '\n');
}

let idCounter = 0;
function nextId() { return ++idCounter; }

// Bij start: announce capabilities
send({
  jsonrpc: '2.0',
  method: 'capabilities',
  params: {
    name: 'github-demo',
    version: '0.0.1',
    resources: ['repo:file'],
    tools: ['createIssue'],
    prompts: ['repo-summary']
  }
});

// Read line-by-line van stdin (vereenvoudigd)
let buffer = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => {
  buffer += chunk;
  let index;
  while ((index = buffer.indexOf('\n')) >= 0) {
    const line = buffer.slice(0, index).trim();
    buffer = buffer.slice(index + 1);
    if (!line) continue;
    handleMessage(line);
  }
});

async function handleMessage(line) {
  let msg;
  try { msg = JSON.parse(line); } catch (e) { return; }

  if (msg.method === 'getResource') {
    const { name, params } = msg.params || {};
    if (name === 'repo:file') {
      try {
        const { owner, repo, path } = params;
        const res = await octo.request('GET /repos/{owner}/{repo}/contents/{path}', { owner, repo, path });
        const content = Buffer.from(res.data.content, res.data.encoding).toString('utf8');
        return send({ jsonrpc: '2.0', id: msg.id, result: { mime: 'text/plain', data: content } });
      } catch (e) {
        return send({ jsonrpc: '2.0', id: msg.id, error: { code: -32001, message: e.message } });
      }
    }
  }

  if (msg.method === 'callTool') {
    const { name, params } = msg.params || {};
    if (name === 'createIssue') {
      try {
        const { owner, repo, title, body } = params;
        const issue = await octo.request('POST /repos/{owner}/{repo}/issues', { owner, repo, title, body });
        return send({ jsonrpc: '2.0', id: msg.id, result: { number: issue.data.number, url: issue.data.html_url } });
      } catch (e) {
        return send({ jsonrpc: '2.0', id: msg.id, error: { code: -32002, message: e.message } });
      }
    }
  }

  if (msg.method === 'getPrompt') {
    const { name } = msg.params || {};
    if (name === 'repo-summary') {
      return send({ jsonrpc: '2.0', id: msg.id, result: {
        template: 'Geef een samenvatting van bestand {{path}} in repo {{owner}}/{{repo}}',
        variables: ['owner','repo','path']
      }});
    }
  }

  // Onbekende method
  if (msg.id) {
    send({ jsonrpc: '2.0', id: msg.id, error: { code: -32601, message: 'Method not found' } });
  }
}

process.on('SIGINT', () => process.exit(0));
