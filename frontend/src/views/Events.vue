<template>
  <v-content>
    {{ info }}
  </v-content>
</template>

<script>
export default {
    name: 'Events',
    data: () => ({
      'info': null
    }),
    created() {
      this.loadEvents();
    },
    methods: {
      loadEvents() {
        this.$http.get('events').then(res => (this.info = res.data))
        .catch(e => {
          console.log(e);
        });
      }
    }
}
</script>