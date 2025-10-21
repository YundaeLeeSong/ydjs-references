using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Waypoint : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        WayPointCounter counter = other.GetComponent<WayPointCounter>();
        if (counter != null)
        {
            counter.CollectWaypoint(gameObject); // Collect the waypoint
        }
    }
}
