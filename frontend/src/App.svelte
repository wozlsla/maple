<script>
  let posts_list = []; // init

  function get_posts() {
    fetch("http://127.0.0.1:8000/api/board/list").then((response) => {
      response.json().then((json) => {
        posts_list = json;
      });
    });
  }

  get_posts();
</script>

<ul>
  {#each posts_list as post}
    <li>{post.title}</li>
  {/each}
</ul>
