
var Game = {};

Game.init = function() {
    game.stage.disableVisibilityChange = true;
}
    
Game.preload = function() {
    game.stage.backgroundColor = "#00cc00";
    game.load.spritesheet('warrior-right','../static/img/warrior-right.png',160,160,8);
    game.load.spritesheet('warrior-left','../static/img/warrior-left.png',160,160,8);
    game.load.tilemap('map', '../static/img/example_map.json', null, Phaser.Tilemap.TILED_JSON);
    game.load.spritesheet('tileset', '../static/img/tilesheet.png',32,32);
    //game.load.image('sprite','../static/img/sprite.png'); // this will be the sprite of the players

}

Game.create = function () {
    var map = game.add.tilemap('map');
    map.addTilesetImage('tilesheet', 'tileset'); // tilesheet is the key of the tileset in map's JSON file
    var layer;
    for(var i = 0; i < map.layers.length; i++) {
        layer = map.createLayer(i);
    }
    layer.inputEnabled = true; // Allows clicking on the map
}