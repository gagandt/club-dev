<template>
  <v-card flat>
    <v-toolbar
      dark
      extended
      flat
      overflow: hidden
      height="800"
    >
    </v-toolbar>

    <v-card

      max-width="700"
      style="margin-top: -760px; margin-left: 300px;"
      dark
    >
      <v-toolbar flat>
        <v-toolbar-title>Get Song Recommendations</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </v-toolbar>
      <v-divider></v-divider>
        
      <v-card-text style="height: 230px;" >
          <v-select
            v-model="genre"
            :items="items"
            label="Select an option">
          </v-select>
          <v-spacer></v-spacer>
          <v-btn color="teal" @click="getsongs">
            Get Songs
            <v-icon dark right>headset</v-icon>
          </v-btn><br><br>
          <h3 class="cap" v-for ="item in info" :key="item.Id" v-on:click="link(item)">
            {{ item.Song }} by {{ item.Artist}}
          </h3>
              
      </v-card-text>
    </v-card>
  </v-card>
</template>


<script>
export default {
    name: "GetSong",
    data: () => {
      return ({
        items: ["rock","metal","pop"],
        genre: "",
        info: {},
        claims: ""
      });
    },
    created () { this.setup() },
    methods: {
      link: function (item) {
        var ref = "https://www.youtube.com/results?search_query=" + item.Song + " by " + item.Artist;
        window.open(ref);
      },
      getsongs() {
        this.$http.get('events/' + this.genre + '/check').then(res => {
          this.info = res.data;
        })
        .catch(e => {
          console.log(e);
        });
      },
      
    }
}
</script>

<style scoped>
  v-card {
    overflow: hidden;
  }
  .cap {
    text-transform: capitalize;
    font-family: sans-serif;
    
  }
  .cap:hover {
    cursor: pointer;
    color: purple;
  }
</style>