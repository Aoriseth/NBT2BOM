NBT reader for minecraft
========================

This is a python implementation which reads data from nbt files and prints out a bill of materials to show the required blocks to build this nbt schematic.

WIP
---
nbt files using a pallete will not read in correctly



More information about NBT format:
==================================

https://minecraft.gamepedia.com/Structure_block_file_format

NBT Structure

    : The root tag.
         DataVersion: Version of the NBT structure.
         author: Name of the player who created this structure, only exists for structures saved before 1.13.
         size: 3 TAG_Int describing the size of the structure
         palette: Set of different block states used in the structure.
            : Block state
                 Name: Id of the block
                 Properties: List of block state properties, with [name] being the name of the block state property
                     Name: The block state name and it's value.
         palettes: Sets of different block states used in the structure, a random palette gets selected based on coordinates and structure integrity. Used in vanilla by shipwrecks.
            : A set of different block states used in the structure.
                : Block state
                     Name: Id of the block
                     Properties: List of block state properties, with [name] being the name of the block state property
                         Name: The block state name and it's value.
         blocks: List of individual blocks in the structure.
            Individual block
                 state: Index of the block state in the palette
                 pos: 3 TAG_Int describing the position of this block
                 nbt: nbt of the associated block entity (optional, only present if the block has one). Does not contain x, y, or z fields. See Block entity format.
         entities: List of entities in the structure
            : Entity
                 pos: 3 TAG_Double describing the exact position of the entity
                 blockPos: 3 TAG_Int describing the block position of the entity
                 nbt: nbt of the entity (required). See entity format.

