<template>

  <v-row>
    <v-col outlined
      v-for="(user,i) in users"
      :key="i"
      cols="3"
    >
      <v-card
        class="mx-auto"
        max-width="344"
        round
      >
        <v-img
          round
          src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
          height="200px"
        ></v-img>

        <v-card-title>
          {{ user.first_name }} {{ user.last_name}}
        </v-card-title>

        <v-card-title class="subtitle-2 pl-4 pt-0 mt-0">
          2016-2020
        </v-card-title>

        <v-card-actions>
          <v-btn tile outlined class="info">@{{ user.username }}</v-btn>

          <v-btn
            color="success"
            text
          >
            Profile
          </v-btn>

          <v-spacer></v-spacer>

          <v-btn
            icon
            @click="toggleDesc(user)"
          >
            <v-icon>{{ user.show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
          </v-btn>
        </v-card-actions>

        <v-expand-transition>
          <div v-show="user.show">
            <v-divider></v-divider>

            <v-card-text>
              I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
            </v-card-text>
          </div>
        </v-expand-transition>
      </v-card>                        
     
    </v-col>
    
  </v-row>
</template>

<script>
  export default {
    components :{

    },
    data: () => ({
      users: [],
      show: false,    
    }),
    created() {
      this.getAllUsers();
    },
    methods: {
      getAllUsers() {
        this.$http.get('members').then(res => {
          for (let user of res.data)
            user.show = false;
          this.users = res.data;          
        }).catch(e => {
          console.log(e);
        });
      },
      toggleDesc(user) {
        console.log('hjhjh');
        user.show = !user.show;
      }
    }
  }
</script>
