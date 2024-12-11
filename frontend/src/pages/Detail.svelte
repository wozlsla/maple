<script>
  import fastapi from '../lib/api';

  export let params = {};
  let post_id = params.post_id;
  let post = {};

  function get_post() {
    fastapi('get', '/api/board/detail/' + post_id, {}, (json) => {
      post = json;
    });
  }

  get_post();
</script>

<h1>{post.title}</h1>
<div>
  {post.content}
</div>
