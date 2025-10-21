using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class StartMenu : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        BgmManager.Instance.SetVolume(0.3f);
        SfxManager.Instance.SetVolume(0.3f);
        BgmManager.Instance.PlayBGM("Assets/BGMs/bgm01_start.mp3");
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
