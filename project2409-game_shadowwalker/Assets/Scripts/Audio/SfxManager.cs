using UnityEngine;
using UnityEngine.AddressableAssets;
using UnityEngine.ResourceManagement.AsyncOperations;
using System.Collections;
using System.Collections.Generic;

public class SfxManager : MonoBehaviour
{
    private bool isLocked = false;
    public static SfxManager Instance;

    public AudioSource audioSourcePrefab;
    public string[] sfxAddresses;

    private Dictionary<string, AudioClip> loadedSFXClips = new Dictionary<string, AudioClip>();
    private Dictionary<string, AudioSource> loopingAudioSources = new Dictionary<string, AudioSource>();

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
        SetVolume(0.5f); // ininitial volume should be reasonable.
    }

    public void PlaySFX(string address)
    {
        if (isLocked) return;
        if (loadedSFXClips.ContainsKey(address))
        {
            PlayClip(loadedSFXClips[address], false);
        }
        else
        {
            StartCoroutine(LoadAndPlaySFX(address, false));
        }
    }
    public void AbsolutePlaySFX(string address)
    {
        if (loadedSFXClips.ContainsKey(address))
        {
            PlayClip(loadedSFXClips[address], false);
        }
        else
        {
            StartCoroutine(LoadAndPlaySFX(address, false));
        }
    }

    public void PlayLoopingSFX(string address)
    {
        if (isLocked) return;
        if (loopingAudioSources.ContainsKey(address))
        {
            // If already playing, do nothing
            return;
        }

        if (loadedSFXClips.ContainsKey(address))
        {
            PlayClip(loadedSFXClips[address], true, address);
        }
        else
        {
            StartCoroutine(LoadAndPlaySFX(address, true));
        }
    }

    public void StopLoopingSFX(string address)
    {
        if (isLocked) return;
        if (loopingAudioSources.ContainsKey(address))
        {
            AudioSource audioSource = loopingAudioSources[address];
            audioSource.Stop();
            Destroy(audioSource.gameObject);
            loopingAudioSources.Remove(address);
        }
    }

    private IEnumerator LoadAndPlaySFX(string address, bool loop)
    {
        var handle = Addressables.LoadAssetAsync<AudioClip>(address);
        yield return handle;

        if (handle.Status == AsyncOperationStatus.Succeeded)
        {
            AudioClip clip = handle.Result;
            loadedSFXClips[address] = clip;
            PlayClip(clip, loop, address);
        }
        else
        {
            Debug.LogError("Failed to load SFX from address: " + address);
        }
    }

    private void PlayClip(AudioClip clip, bool loop, string address = "")
    {
        AudioSource audioSource = Instantiate(audioSourcePrefab);
        audioSource.clip = clip;
        audioSource.loop = loop;
        audioSource.Play();

        if (loop)
        {
            loopingAudioSources[address] = audioSource;
        }
        else
        {
            Destroy(audioSource.gameObject, clip.length);
        }
    }

    public void SetVolume(float volume)
    {
        audioSourcePrefab.volume = volume;
    }
    public float GetVolume()
    {
        return audioSourcePrefab.volume;
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
