using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class Player : MonoBehaviour
{
    float H; //偏移值
    float F;  //左右翻转
    public int Soul;
    public Text SoulNum;
    public Vector2 velocity;  //向量速度
    public Rigidbody2D player;
    public Collider2D coll;  //获取碰撞器边界
    public float MoveSpeed = 5; //移动速度
    public float JumpSpeed = 15;  //跳跃速度
    public LayerMask ground;  //获取层级
    public LayerMask doublejump;  //获取层级
    public Animator ani;

    void Start()
    {
        player = GetComponent<Rigidbody2D>();
        ani = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        //左右移动
        Movement();
    }

    //移动
    public void Movement()
    {
        H = Input.GetAxis("Horizontal");
        F = Input.GetAxisRaw("Horizontal");

        //左右移动
        if (H != 0)
        {
            player.velocity = new Vector2(H * MoveSpeed * Time.deltaTime, player.velocity.y);
            ani.SetFloat("running", Mathf.Abs(F));
        }
        //镜像翻转
        if (F != 0)
        {
            transform.localScale = new Vector3(F, 1, 1);
        }

        //跳跃
        if (Input.GetKeyDown(KeyCode.W) && coll.IsTouchingLayers(ground))
        {

            player.velocity = new Vector2(player.velocity.x, JumpSpeed * Time.deltaTime);
            if (coll.IsTouchingLayers(doublejump))
            {
                player.velocity = new Vector2(player.velocity.x, 2*JumpSpeed * Time.deltaTime);
            }
        }
    }

    private void OnTriggerEnter2D(Collider2D collition)
    {
        if(collition.tag == "Deadline")
        {
            SceneManager.LoadScene(SceneManager.GetActiveScene().name);
        }

        if(collition.tag == "collection")
        {
            Destroy(collition.gameObject);
            Soul += 1; 
            SoulNum.text = Soul.ToString();
        }
    }

 

}
