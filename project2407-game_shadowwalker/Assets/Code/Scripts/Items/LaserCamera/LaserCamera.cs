using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class LaserCamera : MonoBehaviour
{
    private Animator animator;
    private const string CAMERA_ENABLED = "CameraEnabled";
    private PlayerInputController playerInputController;
    private IceCollector iceCollector;
    public float unfreezeTime;
    public Image iceImage;
    public bool isFreezing = false;
    
    // Start is called before the first frame update
    void Start()
    {
        animator = GetComponent<Animator>();
        animator.SetBool(CAMERA_ENABLED, true);
        playerInputController = GameObject.FindGameObjectWithTag("Player").GetComponent<PlayerInputController>();
        iceCollector = GameObject.FindGameObjectWithTag("Player").GetComponent<IceCollector>();
    }

    // Update is called once per frame
    void Update()
    {
    // if (GameObject.FindGameObjectWithTag("Player").GetComponent<PlayerInputController>().IsFreezing() && player.GetComponent<IceCollector>().hasIce)
    if (playerInputController.IsFreezing() && (iceCollector.hasIce || iceImage.fillAmount > 0))
        {
            Debug.Log("Player is freezing");
            animator.SetBool(CAMERA_ENABLED, false);
            unfreezeTime = Time.time + 30;
            isFreezing = true;
            if (Time.time > unfreezeTime)
            {
                animator.SetBool(CAMERA_ENABLED, true);
                iceCollector.hasIce = false;
                isFreezing = false;
                iceImage.fillAmount = 0;
            }
            else {
                iceImage.fillAmount = (unfreezeTime - Time.time) / 30;
            }
        }
    }
}
