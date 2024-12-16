<script>
  import { push } from 'svelte-spa-router';
  import fastapi from '../lib/api';
  import Error from '../components/Error.svelte';

  let error = { detail: [] };
  let title = '';
  let content = '';

  function add_post(event) {
    event.preventDefault();
    let url = '/api/v1/board/post';
    let params = {
      title: title,
      content: content,
    };
    fastapi(
      'post',
      url,
      params,
      (json) => {
        push('/');
      },
      (json_error) => {
        error = json_error;
      }
    );
  }
</script>

<div class="container">
  <h5 class="my-3 border-bottom pb-2">글쓰기</h5>
  <Error {error} />

  <form method="post" class="my-3">
    <div class="mb-3">
      <label for="title">제목</label>
      <input type="text" class="form-control" bind:value={title} />
    </div>

    <div class="mb-3">
      <label for="content">내용</label>
      <textarea class="form-control" rows="10" bind:value={content}></textarea>
    </div>

    <button class="btn btn-primary" on:click={add_post}>저장</button>
  </form>
</div>
