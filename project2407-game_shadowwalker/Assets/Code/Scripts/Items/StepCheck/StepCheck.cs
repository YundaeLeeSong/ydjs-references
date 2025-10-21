using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class StepCheck : MonoBehaviour
{
    public bool crossed = false;
    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            crossed = true;
        }
    }
}
