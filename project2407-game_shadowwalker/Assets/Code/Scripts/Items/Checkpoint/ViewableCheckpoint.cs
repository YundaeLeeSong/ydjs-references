using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ViewableCheckpoint : MonoBehaviour
{
    // Start is called before the first frame update

    public GameObject player;
    public float dot = 0.0f;
    public float angle = 0.0f;

    public bool playerInFront = false;

    void Start()
    {
        Vector3 dir = (player.transform.position - transform.position).normalized;
        dot = Vector3.Dot(dir, player.transform.forward);
        angle = Vector3.Angle(dir, player.transform.forward);
    }

    // Update is called once per frame
    void Update()
    {
        Vector3 dir = (player.transform.position - transform.position).normalized;
        dot = Vector3.Dot(dir, player.transform.forward);
        angle = Vector3.Angle(dir, player.transform.forward);
        if (dot < -0.9f && playerInFront == false)
        {
            playerInFront = true;
            Debug.Log("Player is in front of the checkpoint");
        }
    }
}
