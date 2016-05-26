/**
 * Created by octo on 25-May-16.
 */

function isInModal(curElement,modalId){
    do{
        curElement=curElement.parentElement;
        if(curElement==null)
            return false;
        if(curElement.id==modalId) {
            return true;
        }
    } while(curElement!=null)
    return false;
}

function navigateToUrl(characterUrl, currentElement, parentModalId){
        if(!isInModal(currentElement,parentModalId)) {
        window.location.replace(characterUrl);
    }
    else{
        id="#"+parentModalId;
        $.get( characterUrl, function( data ) {
            $( id ).html( data );
        });
    }
}