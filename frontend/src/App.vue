<template>
  <v-app id="app">
    <v-navigation-drawer
      v-model="primaryDrawer.model"
      clipped
      app
      overflow
    >
      <navigation />
    </v-navigation-drawer>

    <v-app-bar
      clipped-left
      app
      height="80px"
      style="padding-left: 20px"
    >
      <v-app-bar-nav-icon
        @click.stop="primaryDrawer.model = !primaryDrawer.model"
      />
      
      <v-toolbar-title
        class="font-weight-bold"
      >  
        <v-img
          :src="require('./assets/image.png')"
          class="my-03"
          contain
          width="80"
          height="80"
        ></v-img>
      </v-toolbar-title>
      <v-toolbar-title
        class="font-weight-bold"
      >
        Music Society, IIT Mandi
      </v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container fluid>
        <v-row
          align="center"
          justify="center"
        >
          <v-col cols="11">
            <v-card>
              Content
              <router-view />
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>

    <v-footer
      app
    >
      <span class="px-4">&copy; {{ new Date().getFullYear() }}: Music Society, IIT Mandi</span>
    </v-footer>
  </v-app>
</template>

<script>
  import Navigation from './components/Navigation.vue';
  export default {
    components :{
      Navigation
    },
    data: () => ({
      primaryDrawer: {
        model: null,
      },
    }),
    created() {
      this.$vuetify.theme.dark = true;
    }
  }
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
