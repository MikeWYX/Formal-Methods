Lemma ex1: forall A:Prop, 
~~~A -> ~A.
Proof.
intro h1.
intro h2.
intro h3.
apply h2.
intro h4.
apply h4.
assumption.
Qed.
