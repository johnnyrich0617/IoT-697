
Router.configure({
    layoutTemplate:'mainLayout'
});

// Default route
Router.route('/',function() {
    Router.go('home');
});

Router.route('/home',function() {
    this.render('home');
});

Router.route('/dashboard',function() {
    this.render('dashboard');
});