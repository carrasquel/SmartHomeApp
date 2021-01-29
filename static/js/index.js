new Tulipan({
  el: '#app',
  data: {
  },

  ready: function(){
    this.$router.navigate("/main");
  },

  methods: {
  }
})

new Tulipan({
  template: {
    url: "/main",
    async: false
  },

  route: "/main",
  data: {
    temp: 0.0,
    desired_temp: 0.0,
    on: false
  },

  methods: {
    after: function(){
      this.fetchState();
    },
    fetchState: function () {
      this.$http.get('/api/state')
        .then(function (res){
          var data = res.data;
          this.$set("temp", data.temp);
          this.$set("desired_temp", data.desired_temp);
          this.$set("on", data.on);
        }, function(err){
          console.log(err);
        }) 
    },
    routeSettings: function(){
      this.$router.navigate("/settings");
    }
  }
})


new Tulipan({
  template: {
    url: "/settings",
    async: false
  },

  route: "/settings",
  data: {
    desired_temp: 0.0,
    on_1: "",
    off_1: "",
    on_2: "",
    off_2: ""
  },

  methods: {
    after: function(){
      this.fetchSettings();
    },
    fetchSettings: function () {
      this.$http.get('/api/settings')
        .then(function (res){
          var data = res.data;
          this.$set("desired_temp", data.desired_temp);
          this.$set("on_1", data.on_1);
          this.$set("off_1", data.off_1);
          this.$set("on_2", data.on_2);
          this.$set("off_2", data.off_2);
        }, function(err){
          console.log(err);
        })
    },
    postSettings: function(){
      var payload = {
        desired_temp: this.desired_temp,
        on_1: this.on_1,
        off_1: this.off_1,
        on_2: this.on_2,
        off_2: this.off_2
      };
      this.$http.post("/api/settings", payload)
      .then(function(res) {
          this.routeMain();
      }, function(err) {
          this.$loading.hide();
          console.log(err);
      })
    },
    routeMain: function(){
      this.$router.navigate("/main");
    }
  }
})