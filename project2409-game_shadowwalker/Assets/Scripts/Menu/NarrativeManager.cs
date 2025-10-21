using UnityEngine;
using UnityEngine.UI;
using UnityEngine.AddressableAssets;
using UnityEngine.ResourceManagement.AsyncOperations;
using UnityEngine.SceneManagement;
using System.Collections.Generic;
using TMPro;
using System.Collections;

public class NarrativeManager : MonoBehaviour
{
    private float waitTime = 0.3f;
    public string sceneNameToStart;
    public static NarrativeManager Instance { get; private set; }

    public Image narrativeImage;
    public TMP_Text narrativeText;
    public TMP_Text nextButtonText;
    public TMP_Text skipButtonText;

    public List<AssetReference> narrativeSprites;
    public List<AssetReference> narrativeTexts;

    private int currentIndex = 0;

    void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            //DontDestroyOnLoad(gameObject); // singleton
        }
        else
        {
            Destroy(gameObject);
        }
    }

    void Start()
    {
        nextButtonText.transform.parent.GetComponent<UnityEngine.UI.Button>().onClick.AddListener(OnNextButtonClicked);
        skipButtonText.transform.parent.GetComponent<UnityEngine.UI.Button>().onClick.AddListener(OnSkipButtonClicked);
        UpdateNarrative();
    }

    public void ShowNextNarrative()
    {
        currentIndex++;
        if (currentIndex < narrativeSprites.Count)
        {
            UpdateNarrative();
        }
        else
        {
            StartScene();
        }
    }

    void OnNextButtonClicked()
    {
        ShowNextNarrative();
    }

    void OnSkipButtonClicked()
    {
        StartScene();
    }

    void UpdateNarrative()
    {
        if (currentIndex < narrativeSprites.Count)
        {
            narrativeSprites[currentIndex].LoadAssetAsync<Sprite>().Completed += OnSpriteLoaded;
            narrativeTexts[currentIndex].LoadAssetAsync<TextAsset>().Completed += OnTextLoaded;
        }
    }

    void OnSpriteLoaded(AsyncOperationHandle<Sprite> handle)
    {
        if (handle.Status == AsyncOperationStatus.Succeeded)
        {
            narrativeImage.sprite = handle.Result;
        }
    }

    void OnTextLoaded(AsyncOperationHandle<TextAsset> handle)
    {
        if (handle.Status == AsyncOperationStatus.Succeeded)
        {
            narrativeText.text = handle.Result.text;
        }
    }

    public void StartScene()
    {
        StartCoroutine(WaitAndStartScene(sceneNameToStart));
    }

    IEnumerator WaitAndStartScene(string sceneName)
    {
        // Temporarily unpause the game to allow the coroutine to run
        float originalTimeScale = Time.timeScale;
        Time.timeScale = 1f;
        Debug.Log("Before waiting 0.3 seconds");
        yield return new WaitForSecondsRealtime(waitTime);
        Debug.Log("After waiting 0.3 seconds");

        Time.timeScale = originalTimeScale; // Restore the original time scale
        SceneManager.LoadScene(sceneName);
    }
}
