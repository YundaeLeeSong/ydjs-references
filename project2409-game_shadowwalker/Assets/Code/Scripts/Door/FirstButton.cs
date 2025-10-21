using System.Collections;
using UnityEngine;

public class FirstButton : MonoBehaviour
{
    public GameObject door; // Assign the Door GameObject in the Inspector
    public Vector3 openPosition = new Vector3(70.6706f, 3.503326f, -11.46f); // Position when the door is open
    public Vector3 closedPosition = new Vector3(70.6706f, 1.833326f, -11.46f); // Position when the door is closed
    public float moveSpeed = 2f; // Speed at which the door moves

    private bool isPlayerNear = false;
    private bool isDoorOpen = false;
    private Coroutine moveCoroutine;
    private PlayerInputController playerInputController;

    void Start()
    {
        playerInputController = GameObject.FindGameObjectWithTag("Player").GetComponent<PlayerInputController>();
    }

    void Update()
    {
        if (isPlayerNear && playerInputController.IsUsing())
        {
            if (moveCoroutine != null)
            {
                StopCoroutine(moveCoroutine);
            }
            if (isDoorOpen)
            {
                moveCoroutine = StartCoroutine(MoveDoor(closedPosition.y));
            }
            else
            {
                moveCoroutine = StartCoroutine(MoveDoor(openPosition.y));
            }
            isDoorOpen = !isDoorOpen;
        }
    }

    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            isPlayerNear = true;
        }
    }

    void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            isPlayerNear = false;
        }
    }

    private IEnumerator MoveDoor(float targetY)
    {
        float elapsedTime = 0f;
        Vector3 startingPosition = door.transform.position;

        while (elapsedTime < 1f)
        {
            float newY = Mathf.Lerp(startingPosition.y, targetY, elapsedTime * moveSpeed);
            door.transform.position = new Vector3(startingPosition.x, newY, startingPosition.z);
            elapsedTime += Time.deltaTime;
            yield return null; // Pause execution here and continue in the next frame
        }

        door.transform.position = new Vector3(startingPosition.x, targetY, startingPosition.z); // Ensure the door ends exactly at the target position
    }
}
