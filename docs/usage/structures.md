# Structures

The clipboard is a very useful feature, but sometimes you may find you need quick and easy access to a build, or a part of one. This is where structures come in.

[TOC]

## Making a structure

Creating a structure is very simple. Just select a region you want to save for later, and run the command `;export <name>`. Now the region you selected has been saved permanently; even if you exit the world and come back.

!!! Note
    `<name>` should not have any special characters or spaces in it. Also, you can add an optional namespace to it, in case you are working with multiple structures with the same name. Eg: `mystruct:struct_name`

## Using structures

To use structures, all you have to do is run `;import <name>`. When you do this, the structure will be added to your clipboard. And when holding the kit paste tool, you can see exactly where the structure will be when you paste it! The namespace used when exporting doesn't _need_ to be defined, but if you have multiple structures with the same name, it will be needed to determine which one you're referring to.

!!! Note
    Imported structures cannot be manipulated as much as clipboards can. They always have air, and the rotate and flip operations are more limited.

## Transferring structures to other worlds

As they are, the structures defined when exporting can only be used in the world it was exported in. To use it in other worlds, the original world will need to be processed with an external app. Currently this app is only available for Windows.

More detail coming soon...