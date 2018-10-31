# bucket
Modernized Python version of Bucket in the style of XKCD's IRC Bucket, with chat integrations

The database has not been tested yet, amongst other things. I wouldn't try this at home yet, unless you know what you are doing.

What is bucket?
---------------

Very similar to [xkcd-Bucket](https://github.com/zigdon/xkcd-bucket), bucket is a bot that can be
taught factoids that will be triggered when certain phrases are said. Not all of the features of Bucket
have been implemented, but that is a goal for this project. The following guide is a brief overview on 
how to get started, a full wiki is in the works.

In order to teach bucket, you must address him directly by saying "bucket, " + command, or whatever
you name your bucket.

One of the important departures from the original bucket is the modularity of the project. Different features
can be used and managed via chat commands by adding custom modules. They will be in constant development; stay tuned.

Development
-----------
Check out the wiki page

Installing
----------

The following installation instructions are assuming you are using an ubuntu server.

1. Clone this repository.

2. Install 
  TODO

3. Pre-flight checklist
  TODO

4. Start bucket.
  TODO

10. Start adding factoids!

What can bucket do?
-------------------

The very basic functionality of bucket remains similar to xkcd Bucket.

### Factoids

#### X is Y

This is the most common and basic method of teaching bucket factoids, it is added by simply saying `X is Y`. 
If "X" is said later, bucket will reply with "X is Y". Be careful, though, as it is also easy to accidentally
create factoids this way.

`X is Y is Z` will be split between `X` and `Y`, and bucket will respond to the trigger "X" with "X is Y is Z."
`X is Y <is> Z` must be used for "X is Y" to trigger "X is Y is Z." See the section on <verb>s below.

#### X are Y

This is used identically to `X is Y`, with the exception being that bucket will respond to "X" with "X are Y."

#### X \<verb\> Y

bucket is smart enough to know verbs! `X loves Y` and similar phrases will cause X to trigger "X loves Y."

`X<'s> Y` is a special variant of this, making "X" trigger "X's Y."

#### X \<reply\> Y

Perhaps the second-most used factoids are `X <reply> Y` factoids. Saying "X" will make bucket respond "Y."

#### X \<action\> Y

This will make bucket use a `/me` when he replies. Thus, saying "X" will make bucket `/me Y`.

#### Commands

bucket is not a client! Teaching him factoids such as `Quit <reply> /quit` will not work as intended.

#### Quotes

TODO

bucket has the ability to remember things that users have said. `Remember {nick} {snippet_from_line}` will remember
that user's line under the trigger "nick quotes."

### Searching and Editing

#### Listing

TODO

`literal X` will list all the factoids associated with that trigger, separated by `|`. If there are too many, bucket
will automatically create a new page and append "*n* more." `literal[*p*] X` will list page number *p*.

`literal[*] X` will make bucket produce a URL of a text file with all of the associated factoids.

`X =~ /m/` will make bucket reply with the first factoid in trigger "X" containing "m."

"what was that?" will make bucket list the last spoken factoid with all of its details: "That was X(#000): <reply> Y", the
number being the factoid ID.

#### Editing

TODO

`X =~ s/m/n/` will replace "m" with "n" in the trigger "X." `X =~ s/m/n/i` (adding an "i" flag) will replace case-insensitively.
If there is more than one appearance of "m" in "X," it will replace the first instance. Channel operators can add a "g" flag to 
replace all.

`undo last` undoes the last change to a factoid. Non-ops can only `undo last` if they made the last change.

#### Variables

TODO

Variables will *only* work in responses. 

`$noun` and `$nouns` will add random noun(s) where they are placed.

`$verb`, `$verbed` and `$verbing` will do similarily with verbs.

`$adjective` and `$preposition` have similar effects.

`$who` will be replaced with the person who triggered the factoid, while `$someone` will choose a (semi-)random user.

`$to` will be replaced by the intended recipient, for example, `<someuser> anotherguy: blah blah` will replace $to with "anotherguy."

bucket also has gender variables (among other variables).

#### Inventory

TODO

Items can be put in bucket, given to bucket, or items given to bucket. bucket is also smart enough to understand posession, and will
add "username's item" appropriately. bucket's inventory can be listed with the command `inventory`.

Ops can delete items using `detailed inventory` and `delete item #x`.

`$item`, `$giveitem`, and `$newitem` are all variables concerning items. `$item` will use an item in bucket's inventory, `$giveitem` will
use an item and discard it, and `$newitem` will use a random item from previously learned items.

#### Special Factoids

TODO
bucket also has some factoids for hard-coded uses. These include "Don't Know", "Automatic Haiku" and "Band Name Reply."

#### Contacting

Please contact itsallvoodoo for any bugs, issues, suggestions, or questions. I am looking for active developers, so don't be afraid to fork
it and improve bucket! Many thanks go out to [zigdon](https://github.com/zigdon) for sharing the original inspiration for this irc bot.
