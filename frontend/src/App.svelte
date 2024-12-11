<script>
  import Router from 'svelte-spa-router';
  import Home from './pages/Home.svelte';
  import Detail from './pages/Detail.svelte';

  // svelte-spa-router에서는 반드시 routes라는 이름을 사용해야 함
  const routes = {
    '/': Home,
    '/detail/:post_id': Detail,
  };

  // console.log("라우트 설정:", routes); // 라우트 설정 확인
  // console.log("Home 컴포넌트:", Home); // Home 컴포넌트 임포트 확인
</script>

<Router {routes} />
