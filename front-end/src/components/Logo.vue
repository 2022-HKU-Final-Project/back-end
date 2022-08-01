<template>
  <div class="logo">
    <img src="@/assets/logo.png" width="85px" height="70px" />
  </div>
</template>
<script>
export default {
  name: "logo",
  props: {
    isTransparent: {
      type: Boolean,
      default: false,
    },
  },
};
</script>
