<script>
  import fastapi from '../lib/api';
  import Error from '../components/Error.svelte';

  export let params = {};
  let post_id = params.post_id;
  let post = { comment: [] };
  let content = '';
  let error = { detail: [] };

  function get_post() {
    fastapi('get', '/api/board/detail/' + post_id, {}, (json) => {
      post = json;
    });
  }

  get_post();

  function post_comment(event) {
    event.preventDefault();
    let url = '/api/board/detail/' + post_id + '/comment';
    let params = {
      content: content,
    };
    fastapi(
      'post',
      url,
      params,
      (json) => {
        content = '';
        error = { detail: [] };
        get_post();
      },
      (err_json) => {
        error = err_json;
      }
    );
  }
</script>

<h1>{post.title}</h1>
<div>
  {post.content}
</div>

<ul>
  {#each post.comment as comt}
    <li>{comt.content}</li>
  {/each}
</ul>
<Error {error} />

<form method="post">
  <textarea rows="15" bind:value={content}></textarea>
  <input type="submit" value="답변등록" on:click={post_comment} />
</form>
