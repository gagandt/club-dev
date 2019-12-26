<template>
  <v-list
    shaped
    style="padding-top:20px"
  >
    <v-list-item-group 
      v-model="item"
      color="pink" 
      style="align-self:left"
    >
      <v-list-item
        v-for="(item, i) in items"
        :key="i"
        style="align-self:left"
        @click="changeRoute(item)"
      >
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>
        <span class="font-weight-bold"> {{ item.text }} </span>
      </v-list-item>
    </v-list-item-group>
  </v-list>
</template>

<script>
  import router from "../router";

  export default {
    data: () => ({
      item: 0,
      items: [
        { icon: 'music_video', text: 'Videos'},
        { icon: 'mdi-calendar-multiple', text: 'Events', route: '/events'},
        { icon: 'mdi-music-circle', text: 'Originals'},
        { icon: 'queue_music', text: 'Curated Playlists'},
        { icon: 'mdi-contacts', text: 'Members', route: '/auth'},        
        { icon: 'mdi-settings', text: 'Settings' },
        { icon: 'mdi-discord', text: 'Discussion' },
        { icon: 'info', text: 'About', route: '/about' },
      ],
    }),
    methods: {
      changeRoute(item) {
        if (item.route)
          if (item.route != '/home')
            router.push(item.route);
      }
    }
  }
</script>