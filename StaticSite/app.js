angular.module('craneStatic.app', [])
    .controller('craneController', function() {
      var ctrl = this;

        ctrl.action = function(dir) {
            console.log(dir);
        }
    })
    .run(function() {
        console.log("Startup");
    });
