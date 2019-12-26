<template>
  <v-content>
   
    
    
      
    
          <v-card
            width="1000"
            max-width="800"
            height="800"
            style="margin-top: 10px;"
            dark
          >
            <v-toolbar>
              <v-toolbar-title > Add a Song to Your Song Recommendations</v-toolbar-title>
              <v-spacer />
            </v-toolbar>
            <v-card-text>
              <v-form 
                ref="form"
                v-model="valid"
                lazy-validation
              >
                <v-container>
                  <v-text-field                    
                    v-model="credentials.Song"
                    prepend-icon="headset" 
                    :counter="70"
                    label="Song"
                    :rules="rules.Song"
                    maxlength="70"
                    required
                  />
                  <v-text-field
                    v-model="credentials.Artist"
                    prepend-icon="person" 
                    :counter="70"
                    label="Artist"
                    :rules="rules.Artist"
                    maxlength="70"
                    required
                  />
                  <v-text-field                    
                    v-model="credentials.Genre"
                    prepend-icon="headset" 
                    :counter="70"
                    label="Genre -- only rock, metal or pop"
                    :rules="rules.Genre"
                    maxlength="70"
                    required
                  />
                </v-container>
              </v-form>
          
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn
                color="teal"
                @click="login"
              >
                Add
              <v-icon dark right>mdi-checkbox-marked-circle</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
       
  </v-content>
</template>

<script>
import axios from 'axios';
import swal from 'sweetalert2';
import router from '../../router';
export default {
    name: 'AddSong',
    created() {
          this.checkLoggedIn();
        },
    data: () => ({
        drawer: null,
        items: [
          { title: 'Home', icon: 'house' },
          { title: 'Get Songs', icon: 'headset' },
          { title: 'LogOut', icon: 'mdi-export'}
        ],
        credentials: {},
        name: sessionStorage.getItem("username"),
        valid:true,
        loading:false,
        rules: {
          Song: [
            v => !!v || "Required",
            v => /^[A-Z a-z 0-9_]+$/.test(v) || "Artist can only contain letters and digits"
          ],
          Artist: [
            v => !!v || "Required",
          ],
          Genre: [
            v => !!v || "Required",
            v => /^[a-z 0-9_]+$/.test(v) || "Genre can only contain small letters"
          ]
        }
    }),
    methods: {
        checkLoggedIn() {
          this.$session.start();
          if (!this.$session.has("token")) {
            router.push("/auth");
          }
        },

        LinkTo: function (item) {
          var ref = "";
          if (item.title == "Home") {
            ref = "http://localhost:8080/"
          }
          else if (item.title == "Get Songs") {
            ref = "http://localhost:8080/getsong/"
          }
          else if (item.title == "LogOut") {
            this.$session.destroy();
            ref = "http://localhost:8080/auth";
          }
         window.location.href = ref;
        },

        login() {
          if (this.$refs.form.validate()) {
              this.loading = true;
              axios.defaults.headers.common['Authorization'] = 'Token ' + this.$session.get('token');
              axios.post('http://localhost:8000/events/addsong/', this.credentials).then(res => {
                
                alert("Your Song has been added.")
                console.log(res);
                get_name();
                location.reload();
              }).catch(e => {
                this.loading = false;
                console.log(e);
              });
            }
        }    
    }
    
}
</script>

<style scoped>
  .tool {
    margin-top: 0px;
  }
</style>