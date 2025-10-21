using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WayPointCounter : MonoBehaviour
{
    private List<GameObject> collectedWaypoints = new List<GameObject>();
    public int waypointCount = 0;

    public void CollectWaypoint(GameObject waypoint)
    {
        if (!collectedWaypoints.Contains(waypoint))
        {
            collectedWaypoints.Add(waypoint);
            waypointCount++;
            Destroy(waypoint);
            Debug.Log("Collected waypoint. Total: " + waypointCount);
        }
    }

    public void ResetWaypoints()
    {
        collectedWaypoints.Clear();
        waypointCount = 0;
        Debug.Log("Waypoints reset.");
    }
}
