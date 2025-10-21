<!-- 
 @requires
 1. VSCode extension: null
 2. Shortcut: 'Ctrl' + 'Shift' + 'V'
 3. Split: Drag to right (->)
 -->
<!-- Anchor Tag (Object) for "back to top" -->
<a id="readme-top"></a>



# Introduction
## Author
- **Team Name (OIT/Canvas Account Name):** Kaleidoscope, Shadow Walker
  - Patil, Akshay V: apatil97@gatech.edu
  - Co, Jadon D: jco9@gatech.edu
  - Chaturvedi, Yash: yash.c@gatech.edu
  - Song, Jaehoon: jsong421@gatech.edu

## Contributions by Team Member
- Akshay: Level Design, Character Animations, Enemy State Machine, Menus, Character Controllers, Level Design, Input Controller, Enemy Animations, Enemy Controllers
- Jadon: Level Design, Waypoints
- Yash: HUD, Collectable Items
- Jaehoon: Audio System, Menu with Controls and Transitions,  2D narrative and objectives UI, README.md

## Main Scene
The main scene of the project is the following.
```
./Assets/Scenes/StartMenu.scene
./Assets/Scenes/Narrative.scene
./Assets/Scenes/GameDemo.scene
./Assets/Scenes/AlphaLevel.scene
```
<p align="right">(<a href="#readme-top">back to top</a>)</p><br /><br /><br />


## Build Observations
The followings are the observations expected by project implementations.
1. **Character Animations using Root Motion**
   - Player input through keyboard and mouse or through a gamepad, (not fully tested as we don't have access to a controller)
   - High quality character animations for walking, crouching, running, jumping, and taking enemies down
   - Character physics such as bumping into crates and falling when walking off a ledge
2. **Enemy AI**
   - Enemy state machine with multiple states (Patrol, Alert, Detected, Dead, etc.)
   - Enemy movement using navmesh agents
   - Enemy animations using root motion
   - Enemies can detect the player based on proximity and player state (running/walking close to an enemy alerts them to the sound created by the player and they will turn around)
3. **Items**
   - Collectable items that add complexity and strategy to the game, (ice blocks to freeze lazer cameras and keys to beat the level)
5. **Audio Integration**
   - Background music (BGM) and sound effects (SFX) integrate smoothly into the Unity project.
   - No noticeable lag or delay when audio assets are played.
6. **Addressables Memory Management**
   - Audio assets are loaded asynchronously using Unity's Addressables system.
   - Performance impact is minimized due to asynchronous loading.
   - Memory usage is optimized for loading and unloading audio assets.
7. **BGM and SFX Managers**
   - Managers handle playback of BGM and SFX efficiently.
   - Looping functionality for BGM is implemented correctly.
   - Volume control is smooth and responsive.
8. **User Interface Integration**
   - HUD for in game state information like stealth and prompts
   - Menu for restarting or quitting the game
   - Audio controls (e.g., volume sliders) are integrated into the UI.
   - User adjustments to audio settings are saved and persistent.
<p align="right">(<a href="#readme-top">back to top</a>)</p><br /><br /><br />

## Assets Edited

### Akshay

**Assets**
- HUD
- Menu
- Player
- Enemy
- Level
- Alpha

**Files**
- CharacterAnimationController.cs
- CharacterAudioController.cs
- EnemyAlertState.cs
- EnemyController.cs
- EnemyDeadState.cs
- EnemyDetectedState.cs
- EnemyPatrolState.cs
- EnemyStateMachine.cs
- IState.cs
- InHearingRangeOfEnemyEvent.cs
- InRangeOfEnemyEvent.cs
- NoiseEvent.cs
- TakedownEvent.cs
- PlayerColliderController.cs
- PlayerInputController.cs
- PlayerMovementController.cs
- PlayerStealthController.cs
- HUD.cs
- Menu.cs
- PlayerInput.inputactions

### Jadon

**Assets**

**Files**

### Yash

**Assets**

**Files**

### Jaehoon

**Assets**
- Menu (In-game, start, end)
- Audio System
- Narrative UI
- Addressables

**Files**
```
./Assets/Scripts/Audio/AudioEventSystem.cs
./Assets/Scripts/Audio/SfxManager.cs
./Assets/Scripts/Audio/BgmManager.cs
./Assets/Scripts/Menu/ButtonManager.cs
./Assets/Scripts/Menu/MenuManager.cs
./Assets/BGMs/bgm01_start.mp3
./Assets/BGMs/bgm02_ingame.mp3
./Assets/BGMs/bgm03_end.mp3
./Assets/SFXs/sfx01_pickup.wav
./Assets/SFXs/sfx02_explosion.wav
./Assets/SFXs/sfx03_laser_shot.wav
./Assets/SFXs/sfx04_magic_spell.wav
./Assets/SFXs/sfx05_power_up.wav
./Assets/SFXs/sfx06_tv_noise.wav
./Assets/SFXs/sfx07_water_drop.wav
./Assets/SFXs/sfx08_ding_dong.wav
./Assets/SFXs/sfx09_electric_spark.wav
./Assets/SFXs/sfx10_wood_hit.wav
./Assets/SFXs/sfx11_mouse_click.wav
./Assets/Sprites/narrative1.jpg
./Assets/Sprites/narrative2.jpg
./Assets/Sprites/narrative3.jpg
./Assets/Texts/narrative1.txt
./Assets/Texts/narrative2.txt
./Assets/Texts/narrative3.txt
```

<p align="right">(<a href="#readme-top">back to top</a>)</p><br /><br /><br />

## Known Issues or Bugs
There are no known bugs or incomplete features.
<p align="right">(<a href="#readme-top">back to top</a>)</p><br /><br /><br />



## Dependencies and External Assets
All the dependencies and external assets are resolved within the solution following the assignment tutorial format. 

- external asset, **Addressables** for efficient asset management and loading. It allows the project to load assets asynchronously, improving performance and resource management.
- external asset, **TextMeshPro** for rendering high-quality text within the project. It provides greater control over text styling and layout compared to the default Unity UI Text.
- external asset, **Mixamo** for high-quality animations and character models.
- external asset, **Footsteps - Essentials**, for character movement audio
<p align="right">(<a href="#readme-top">back to top</a>)</p><br /><br /><br />


# Execution Instructions
The input code is listed as follows.
- To run the game, open the Unity project and play the scene.
  ```
  ./Build/Windows/Kaleidoscope_ShadowWalker.exe
  ```
  ```
  ./Build/OSX/Kaleidoscope_ShadowWalker.app
  ```
- Use '**WASD**'/'**Left Stick**' to move your character.
- Use '**Mouse**'/'**Right Stick**' to look around
- Use '**Space**'/'**Button South**' to jump
- Use '**Q**'/'**Button East**' to takedown enemies
- Use '**E**'/'**Button North**' to use (buttons, elevators, etc.)
- Use '**C**'/'**Left Stick Press**' to crouch
- Use '**Left Shift**'/'**Right Trigger**' to run
- Use '**ESC**' (Escape)/'**Start**' to toggle the in-game menu and pause/resume the game.
- Use '**F**'/'**Right Stick Press**' to use ice cubes to stop laser cameras temporarily.
- Use '**O**'/'**P**' to adjust the volume of sounds.
<p align="right">(<a href="#readme-top">back to top</a>)</p><br /><br /><br />


# Project Information
## License
This project is licensed under CS4455, Georgia Institute of Technology - see the [LICENSE.md](LICENSE.md) file for details.
## Contribution
Contributions are allowed - see the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to get started.
## Acknowledgements
This project currently does not include an acknowledgements section as there were no contributions or funding sources to acknowledge at this stage.
<p align="right">(<a href="#readme-top">back to top</a>)</p><br /><br /><br />
