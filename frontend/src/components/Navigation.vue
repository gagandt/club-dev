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
      <v-list-item v-on:click="logout()">
        <v-list-item-icon>
          <v-icon>mdi-export</v-icon>
        </v-list-item-icon>
        <span class="font-weight-bold"> Logout </span>
      </v-list-item>
    </v-list-item-group><br>
    <h2 style="font-family: monospace">{{ user }} </h2>
  </v-list>
</template>

<script>
  import router from "../router";
  export default {
    data: () => ({
      user: sessionStorage.getItem('username'),
      item: 0,
      items: [
        { icon: 'music_video', text: 'Videos'},
        { icon: 'mdi-calendar-multiple', text: 'Events', route: '/events'},
        { icon: 'mdi-music-circle', text: 'Recommend', route: '/song'},
        { icon: 'queue_music', text: 'Curated Playlists', route: '/getsong'},
        { icon: 'mdi-contacts', text: 'Members', route: '/auth'},        
        { icon: 'mdi-settings', text: 'Settings' },
        { icon: 'mdi-discord', text: 'Discussion' },
        { icon: 'info', text: 'About', route: '/about' },
      ],
    }),
    methods: {
      logout: function () {
        this.$session.destroy();
        this.user = "";
        router.push('/')
      },
      
      changeRoute(item) {
        if (item.route)
          if (item.route != '/home')<v-list-item>
        <v-list-item-icon>
          <v-icon></v-icon>
        </v-list-item-icon>
        <span class="font-weight-bold"> Logout </span>
      </v-list-item>
            router.push(item.route);
      }
    }
  }
</script>
