<template>
  <v-content>
    Hi!
  </v-content>
</template>

<script>
export default {
    name: 'Events',
    data: () => ({
    }),
    created() {
      this.loadEvents();
    },
    methods: {
      loadEvents() {
        this.$http.get('events').then(res => {
          console.log(res.data);
        }).catch(e => {
          console.log(e);
        });
      }
    }
}
</script>