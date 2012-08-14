// document ready functions here

$(document).ready(function() {
    
    
    // comments
    $('#comment_form form').submit(function(){
        
        $.post(
              '/comments/post/',
              $('#comment-form').serialize(),
              function(data) {
                if (data.indexOf("none") != -1){
                    var go = $('input[name="next"]').val();
                    window.location = go;
                }
                else{
                   $('#comment_form').prepend( data );
                }
              }     
        );
        
        
        
        return false;    
        
    });
    
    

    // hide the id_tags multi select because we are going to use our jQuery tag selector!
    $("#id_tags").hide();
    $(".tags-error").hide();
    



    // clicking the welcome menu toggles the user menu drop down
    $(".welcome").click(function(e) {

        e.preventDefault();
        $("#user-menu").toggle();
        $("#id_username").focus();
        

    })


    // update the the hidden #id_tags multi select element with the dropped tags
    function updateTagsList(){

        arr = []

        $("#tag-container li").each(function(){

            var tag = $(this).attr("rel");
            arr.push(tag);

        });

        $("#id_tags").val(arr);

    }
    
    
    // setup the li elements in #select-tags-list as draggable
    $("li", "#select-tags-list").draggable({

        revert: "invalid",
        helper: "clone"   

    });
    
    // setup the #tag-container element as droppable
    $('#tag-container').droppable({
        accept: "li",
        activeClass: "tag-container-hightlight",
        tolerance: "fit",
        drop: function( event, ui ){

            var num_tags = $( "li", "#tag-container" ).length;
            if (num_tags < 5){
                moveTag( ui.draggable );
                $(".tags-error").hide();
            }else{
                $(".tags-error").show().html("Max 5 tags. Please remove a tag before trying to add another.");
            }
            
        }

    });
    
    // set variable for delete icon and create function for moving tags
    // from the tag list holding area to the post tag list
    var delete_icon = "<a href='/' class='ui-icon-delete'>x</a>";
    function moveTag( $item ) {
	$item.fadeOut(function() {
	    var $list = $( "ul", "#tag-container" ).length ?
               $( "ul", "#tag-container" ) :
               $( "<ul class='tags-ul'>" ).appendTo( "#tag-container" );
				
                    $item.append( delete_icon ).appendTo( $list ).fadeIn(function() {
			$item
            		    .animate();
						
                    });

                updateTagsList();
	});
    }
    
    // remove a tag by appending it to #select-tags-list
    function deleteTag( $item ) {
	$item.fadeOut(function() {
	    var $list = $( "ul", "#select-tags-list" );

		$item.appendTo( $list ).fadeIn(function() {
		    $item
			.animate();

                });
	});
    }
    
    // sets up the ability to click on the tag to remove it
    $("ul.tags-ul > li").click(function(e){

        var list_item = $(this);   

        var parentTag = list_item.parents("div").attr('id');   
    
        if (parentTag == "tag-container"){
            list_item
                .find("a.ui-icon-delete").remove()
            list_item.appendTo( "#select-tags-list ul" );
            updateTagsList();
        }
        
        $(".tags-error").hide();
        
        e.preventDefault(); 

    });
    
    $(".dismiss").click(function(e){
        
        e.preventDefault();
        $(this).parent().parent().remove();
        
        
        
    });


})