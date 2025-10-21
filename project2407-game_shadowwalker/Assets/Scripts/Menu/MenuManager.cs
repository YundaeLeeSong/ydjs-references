using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MenuManager : MonoBehaviour
{
    private CanvasGroup canvasGroup;

    void Awake()
    {
        canvasGroup = GetComponent<CanvasGroup>();
        if (canvasGroup == null)
        {
            Debug.LogError("CanvasGroup component missing!");
        }
    }



    // Start is called before the first frame update
    void Start()
    {
        //canvasGroup.interactable = false;
        //canvasGroup.blocksRaycasts = false;
        //canvasGroup.alpha = 0f;
        ////////// set by unity
    }



    void Update()
    {
        if (Input.GetKeyUp(KeyCode.Escape))
        {
            if (canvasGroup.interactable)
            {
                canvasGroup.interactable = false;
                canvasGroup.blocksRaycasts = false;
                canvasGroup.alpha = 0f;
                Time.timeScale = 1f; // Unpause the game
                BgmManager.Instance.Unlock();
                SfxManager.Instance.Unlock();
            }
            else
            {
                canvasGroup.interactable = true;
                canvasGroup.blocksRaycasts = true;
                canvasGroup.alpha = 1f;
                Time.timeScale = 0f; // Pause the game
                BgmManager.Instance.Lock();
                SfxManager.Instance.Lock();
            }
        }
    }
}
