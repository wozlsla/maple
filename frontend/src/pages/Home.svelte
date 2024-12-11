<script>
  import fastapi from '../lib/api';
  import { link } from 'svelte-spa-router';

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
    <!-- use:link ~/#/detail -->
    <li><a use:link href="/detail/{post.id}">{post.title}</a></li>
  {/each}
</ul>
