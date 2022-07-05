<template>
  <div class="logo">
    <img src="@/assets/logo.png" width="150px" height="120px">
  </div>
</template>
<script>
export default {
  name: "logo",
  props: {
    isTransparent: {
      type: Boolean,
      default: false
    }
  }
};
</script>
