using UnityEngine;

public class CharacterAudioController : MonoBehaviour 
{
    private AudioSource walkAudioSource;
    private AudioSource jumpAudioSource;
    private AudioSource runAudioSource;
    private AudioSource crouchAudioSource;
    void Awake()
    {
        AudioSource[] audioSources = GetComponents<AudioSource>();
        jumpAudioSource = audioSources[0];
        runAudioSource = audioSources[1];
        walkAudioSource = audioSources[2];
        crouchAudioSource = audioSources[3];
    }
    
    void Start()
    {

    }

    void Update()
    {
        
    }
    
    public void WalkEvent()
    {
        walkAudioSource.Play();
    }
    public void RunEvent()
    {
        runAudioSource.Play();
    }
    public void JumpEvent()
    {
        jumpAudioSource.Play();
    }
    public void CrouchEvent()
    {
        crouchAudioSource.Play();
    }

    public void KillEvent()
    {
    }

    public void UseEvent()
    {
    }
}