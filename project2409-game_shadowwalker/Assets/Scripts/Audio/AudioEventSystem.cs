using Unity.VisualScripting;
using UnityEngine;

public class AudioEventSystem : MonoBehaviour
{
    private int volume;
    private const int MAX_VOL = 10;
    private const int MIN_VOL = 0;

    // Flags for enabling/disabling sounds
    public bool enableS;
    public bool enableD;
    public bool enableF;
    public bool enableG;
    public bool enableH;
    public bool enableJ;

    public bool enableUpArrow;
    public bool enableDownArrow;
    public bool enableLeftArrow;
    public bool enableRightArrow;

    public bool enableMouseClick;
    private void Start()
    {
        volume = (int)(10 * BgmManager.Instance.GetVolume());
    }
    private void Update()
    {
        // Background music (synchronous)
        //if (Input.GetKeyDown(KeyCode.B)) BgmManager.Instance.PlayBGM("Assets/BGMs/bgm01_start.mp3");
        //if (Input.GetKeyDown(KeyCode.N)) BgmManager.Instance.PlayBGM("Assets/BGMs/bgm02_ingame.mp3");
        //if (Input.GetKeyDown(KeyCode.M)) BgmManager.Instance.PlayBGM("Assets/BGMs/bgm03_end.mp3");



        // Single sound effects (asynchronous)
        if (Input.GetKeyDown(KeyCode.S) && enableS)
            SfxManager.Instance.PlaySFX("Assets/SFXs/sfx01_pickup.wav");
        if (Input.GetKeyDown(KeyCode.D) && enableD)
            SfxManager.Instance.PlaySFX("Assets/SFXs/sfx02_explosion.wav");
        if (Input.GetKeyDown(KeyCode.F) && enableF)
            SfxManager.Instance.PlaySFX("Assets/SFXs/sfx03_laser_shot.wav");
        if (Input.GetKeyDown(KeyCode.G) && enableG)
            SfxManager.Instance.PlaySFX("Assets/SFXs/sfx04_magic_spell.wav");
        if (Input.GetKeyDown(KeyCode.H) && enableH)
            SfxManager.Instance.PlaySFX("Assets/SFXs/sfx09_electric_spark.wav");
        if (Input.GetKeyDown(KeyCode.J) && enableJ)
            SfxManager.Instance.PlaySFX("Assets/SFXs/sfx10_wood_hit.wav");

        // Looping sound effects (asynchronous)
        if (Input.GetKeyDown(KeyCode.UpArrow) && enableUpArrow)
            SfxManager.Instance.PlayLoopingSFX("Assets/SFXs/sfx05_power_up.wav");
        if (Input.GetKeyUp(KeyCode.UpArrow) && enableUpArrow)
            SfxManager.Instance.StopLoopingSFX("Assets/SFXs/sfx05_power_up.wav");

        if (Input.GetKeyDown(KeyCode.DownArrow) && enableDownArrow)
            SfxManager.Instance.PlayLoopingSFX("Assets/SFXs/sfx06_tv_noise.wav");
        if (Input.GetKeyUp(KeyCode.DownArrow) && enableDownArrow)
            SfxManager.Instance.StopLoopingSFX("Assets/SFXs/sfx06_tv_noise.wav");

        if (Input.GetKeyDown(KeyCode.LeftArrow) && enableLeftArrow)
            SfxManager.Instance.PlayLoopingSFX("Assets/SFXs/sfx07_water_drop.wav");
        if (Input.GetKeyUp(KeyCode.LeftArrow) && enableLeftArrow)
            SfxManager.Instance.StopLoopingSFX("Assets/SFXs/sfx07_water_drop.wav");

        if (Input.GetKeyDown(KeyCode.RightArrow) && enableRightArrow)
            SfxManager.Instance.PlayLoopingSFX("Assets/SFXs/sfx08_ding_dong.wav");
        if (Input.GetKeyUp(KeyCode.RightArrow) && enableRightArrow)
            SfxManager.Instance.StopLoopingSFX("Assets/SFXs/sfx08_ding_dong.wav");

        // Mouse click sound effect
        if (Input.GetMouseButtonDown(0) && enableMouseClick)
            SfxManager.Instance.AbsolutePlaySFX("Assets/SFXs/sfx11_mouse_click.wav");

        // Volume control
        if (Input.GetKeyDown(KeyCode.P))
        {
            if (volume < MAX_VOL) volume++;
            float newVolume = volume / 10.0f;
            BgmManager.Instance.SetVolume(newVolume);
            SfxManager.Instance.SetVolume(newVolume);
        }
        if (Input.GetKeyDown(KeyCode.O))
        {
            if (volume > MIN_VOL) volume--;
            float newVolume = volume / 10.0f;
            BgmManager.Instance.SetVolume(newVolume);
            SfxManager.Instance.SetVolume(newVolume);
        }

        // Example key bindings for locking and unlocking
        if (Input.GetKeyDown(KeyCode.Q)) // Lock both managers
        {
            BgmManager.Instance.Lock();
            SfxManager.Instance.Lock();
        }

        if (Input.GetKeyDown(KeyCode.W)) // Unlock both managers
        {
            BgmManager.Instance.Unlock();
            SfxManager.Instance.Unlock();
        }
    }

    private void OnCollisionEnter(Collision collision)
    {
        // This is an example use-case for guiding how to implement the sound in collision events.
        if (collision.gameObject.CompareTag("Cube"))
        {
            SfxManager.Instance.PlaySFX("Assets/SFXs/sfx02_explosion.wav");
        }
    }
}
