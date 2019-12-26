<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >
      <v-list dense>
        <v-list-item link v-on:click="getsong()" id="getsong">
          <v-list-item-action>
            <v-icon>headset</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Find new Songs</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link v-on:click="addsong()">
          <v-list-item-action>
            <v-icon>headset</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title id="addsong">Recommend a Song</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      clipped-left
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Home</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col class="shrink">
            <v-tooltip right>
              <template v-slot:activator="{ on }">
                <v-btn
                  :href="source"
                  icon
                  large
                  target="_blank"
                  v-on="on"
                >
                </v-btn>
              </template>
              <span>Source</span>
            </v-tooltip>
            <v-tooltip right>
              <template v-slot:activator="{ on }">
                <v-btn
                  icon
                  large
                  href=""
                  target="_blank"
                  v-on="on"
                >
                </v-btn>
              </template>
            </v-tooltip>
          </v-col>
        </v-row>
      </v-container>
    </v-content>

    <v-footer app>
      <span>&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    props: {
      source: String,
    },
    data: () => ({
      drawer: null,
    }),
    created () {
      this.$vuetify.theme.dark = true
    },
    methods: {
      addsong: function () {
        window.location.href = "http://localhost:8080/song/";
      },
      getsong: function () {
        window.location.href = "http://localhost:8080/getsong/";
      }
    }
  }
</script>