<script>
  import fastapi from '../lib/api';
  import { link } from 'svelte-spa-router';

  let posts_list = []; // init
  let size = 15;
  let page = 0;
  let total = 0;
  $: total_page = Math.ceil(total / size);

  function get_posts(_page) {
    let params = { page: _page, size: size };

    fastapi('get', '/api/v1/board/list', params, (json) => {
      posts_list = json.post_list;
      page = _page;
      total = json.total;
    });
  }

  get_posts(0);
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

  <!-- Pagination -->
  <ul class="pagination justyfi-content-center">
    <!-- 이전페이지 -->
    <li class="page-item {page <= 0 && 'disabled'}">
      <button class="page-link" onclick={() => get_posts(page - 1)}>이전</button
      >
    </li>

    <!-- 페이지 번호 -->
    {#each Array(total_page) as _, loop_page}
      {#if loop_page >= page - 2 && loop_page <= page + 3}
        <li class="page-item {loop_page === page && 'active'}">
          <button onclick={() => get_posts(loop_page)} class="page-link"
            >{loop_page + 1}</button
          >
        </li>
      {/if}
    {/each}

    <!-- 다음 페이지 -->
    <li class="page-item {page >= total_page - 1 && 'disabled'}">
      <button class="page-link" onclick={() => get_posts(page + 1)}>다음</button
      >
    </li>
  </ul>

  <a use:link href="/board" class="btn btn-primary">글쓰기</a>
</div>
