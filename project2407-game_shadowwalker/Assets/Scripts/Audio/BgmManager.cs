using UnityEngine;
using UnityEngine.AddressableAssets;
using UnityEngine.ResourceManagement.AsyncOperations;
using System.Collections;

public class BgmManager : MonoBehaviour
{
    private bool isLocked = false;
    public static BgmManager Instance;

    public AudioSource audioSource;
    public string[] bgmAddresses;

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

        audioSource.loop = true; // Ensure looping
        SetVolume(0.5f); // ininitial volume should be reasonable.
    }

    public void PlayBGM(string address)
    {
        if (isLocked) return;
        StartCoroutine(LoadAndPlayBGM(address));
    }

    private IEnumerator LoadAndPlayBGM(string address)
    {
        var handle = Addressables.LoadAssetAsync<AudioClip>(address);
        yield return handle;

        if (handle.Status == AsyncOperationStatus.Succeeded)
        {
            AudioClip clip = handle.Result;
            audioSource.clip = clip;
            audioSource.Play();
        }
        else
        {
            Debug.LogError("Failed to load BGM from address: " + address);
        }
    }

    public void SetVolume(float volume)
    {
        audioSource.volume = volume;
    }
    public float GetVolume()
    {
        return audioSource.volume;
    }
    public void Lock()
    {
        isLocked = true;
    }

    public void Unlock()
    {
        isLocked = false;
    }
}
