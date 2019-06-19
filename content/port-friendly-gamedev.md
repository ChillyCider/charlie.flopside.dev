Title: Port-friendly Gamedev
Date: 2019-5-31 8:57
Category: Blog
Slug: port-friendly-gamedev
Tags: porting, game development, gamedev

> If you program and want any longevity to your work, make a game. all else recycles, but people rewrite architectures to keep games alive. -- Why the Lucky Stiff

I've found myself agreeing with this sentiment recently. But even games sometimes run into the wall of obsolescence. Let's say no one likes your game.
It uses OpenGL 1 exclusively because of some obscure requirement of your audience. Your game might work on some machines, but break on others, e.g. Raspberry
Pi (which I'm pretty sure only supports OpenGL ES 2). If no one likes your game, it won't get ported... And that makes sense. Porting is indeed a taxing effort for
any project.

What if games or programs were intentionally designed to increase the likelihood of porting?

There are some steps I think one could take:

- Use text-based file formats (XML, JSON, YAML, etc.) for most assets.
- Use a scripting language like Lua to code the behaviors things like filters (for image or sound editors), UI behavior (for general programs), or
  powerup effects or enemy behaviors (for games).
- Finally, write Python or Ruby modules for parsing your assets and scripts, so that your fans can easily port your program to a new engine or computing environment.

Anyway, these were just some thoughts I had and wanted to share.😊
