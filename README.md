# flying-f@#k

[![gif with examples][examples-link]][examples-link]

## Motivations

When using [Concourse's Fly CLI](http://concourse.ci/fly-cli.html), you're often forced to `fly login` or `fly sync`, or you have some typo, and it's kind of annoying.

This repo adds a few rules to [thef@#k](https://github.com/nvbn/thefuck) in order to add support for common Fly CLI issues.

## Installation 

Note: *You must already have [thef@#k](https://github.com/nvbn/thefuck) installed on your machine to use these rules.*

To install:

```
brew install thefuck 
mkdir -p ~/.config/thefuck/rules
git clone git@github.com:andrewedstrom/flying-fuck.git 
cd flying-fuck
cp *.py ~/.config/thefuck/rules
```

[examples-link]: https://github.com/andrewedstrom/flying-fuck/raw/master/example.gif
