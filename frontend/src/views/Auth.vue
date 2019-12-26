<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
    >
      <v-card>        
        <v-container
          fluid
          fill-height
        >
          <v-layout
            align-center
            justify-center
            mt-12
          >
            <v-flex
              xs12
              sm8
              md4
              px-auto
              pt-12
              mt-12
            >              
              <v-card class="elevation-12 mt-64">
                <v-toolbar 
                  dark 
                  color="primary"
                >
                  <v-toolbar-title>IIT Mandi Music Society - Login</v-toolbar-title>
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
                        v-model="credentials.username"
                        prepend-icon="person" 
                        :counter="70"
                        label="Username"
                        :rules="rules.username"
                        maxlength="70"
                        required
                      />
                      <v-text-field
                        v-model="credentials.password"
                        prepend-icon="lock" 
                        type="password"
                        :counter="20"
                        label="Password"
                        :rules="rules.password"
                        maxlength="20"
                        required
                      />
                    </v-container>
                  </v-form>
                </v-card-text>
                <v-card-actions>
                  <v-spacer />
                  <v-btn
                    color="primary"
                    @click="login"
                  >
                    Login
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>        
      </v-card>
    </v-dialog>
  </v-row>  
</template>

<script>
import axios from 'axios';
import swal from 'sweetalert2';
import router from '../router';

export default {
    name: 'Auth',
    data: () => ({
        dialog: true,
        credentials: {},
        valid:true,
        loading:false,
        rules: {
          username: [
            v => !!v || "Username is required",
            v => (v && v.length > 3) || "A username must be more than 3 characters long",
            v => /^[a-z0-9_]+$/.test(v) || "A username can only contain letters and digits"
          ],
          password: [
            v => !!v || "Password is required",
            v => (v && v.length > 7) || "The password must be longer than 7 characters"
          ]
        }
    }),
    methods: {
        login() {
          if (this.$refs.form.validate()) {
              this.loading = true;
              axios.post('http://localhost:8000/auth/', this.credentials).then(res => {
                this.$session.start();
                this.$session.set('token', res.data.token);
                router.push('/home');
              }).catch(e => {
                this.loading = false;
                swal({
                  type: 'warning',
                  title: 'Error',
                  text: 'Wrong username or password',
                  showConfirmButton:false,
                  showCloseButton:false,
                  timer:3000
                })
              });
            }
        }
    }
}
</script>