<script>
  import fastapi from '../lib/api';
  let posts_list = []; // init

  function get_posts() {
    fastapi('get', '/api/board/list', {}, (json) => {
      posts_list = json;
    });
  }

  get_posts();
</script>

<ul>
  {#each posts_list as post}
    <li>{post.title}</li>
  {/each}
</ul>
