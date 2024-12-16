<script>
  import fastapi from '../lib/api';
  import { link } from 'svelte-spa-router';

  let posts_list = []; // init

  function get_posts() {
    fastapi('get', '/api/v1/board/list', {}, (json) => {
      posts_list = json;
    });
  }

  get_posts();
</script>

<div class="container my-3">
  <table class="table">
    <thead>
      <tr class="table-dark">
        <th>번호</th>
        <th>제목</th>
        <th>작성일시</th>
      </tr>
    </thead>
    <tbody>
      {#each posts_list as post, i}
        <tr>
          <td>{i + 1}</td>
          <td>
            <a use:link href="/detail/{post.id}">{post.title}</a>
          </td>
          <td>{post.created_at}</td>
        </tr>
      {/each}
    </tbody>
  </table>
  <a use:link href="/board" class="btn btn-primary">글쓰기</a>
</div>
