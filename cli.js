#!/usr/bin/env node

const path = require('path');

const learn = require('learn')

const pkg = require('./package');

const title = 'LEARN SSH';
const description = pkg.description;
const homePage = 'https://github.com/bocoup/learn-ssh';
const theme = {
  menuBgColor: 'black',
  menuFgColor: 'green',
  webBgColor: '#222',
  webFgColor: '#eee',
  webLinkColor: '#adff2f',
  webHeaderColor: '#adff2f',
  logo: path.join(__dirname, 'theme', 'logo.gif')
};
const exercises = [
  'asymmetric-cryptography',
  'ssh-basics',
  'authorized-keys',
  'known-hosts',
  'ssh-key-passphrases',
  'ssh-agent',
  'permission-elevation',
  'your-server'
];
const exercisesDir = path.join(__dirname, 'exercises');
const template = `
  <html lang="en-US">
    <head>
      <title>{{title}}</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style type="text/css">
      html {
        font-family: monospace;
        background-color: ${theme.webBgColor};
        color: ${theme.webFgColor};
      }
      body {
        padding: 1em;
        font-size: 1.5em;
      }
      h1,h2,h3,h4,h5 {
        color: ${theme.webHeaderColor};
      }
      a {
        color: ${theme.webLinkColor};
        text-decoration: none;
      }
      .exercise { padding: .5em 0em; }
      code {
        padding: 0 .25em;
        background-color: #444;
        border-radius: 3px;
      }
      </style>
      {{{head}}}
    </head>
    <body>
      {{{body}}}
    </body>
  </html>
`;

learn({
  title,
  description,
  homePage,
  theme,
  exercisesDir,
  exercises,
  template
});
