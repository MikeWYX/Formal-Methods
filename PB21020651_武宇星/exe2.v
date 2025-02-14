Lemma ex2: forall A B:Prop, 
A \/ B -> ~ (~ A /\ ~ B).
Proof.
intro h1.
intro h2.
intro h3.
intro h4.
destruct h4 as (h5, h6).
destruct h3 as [h7 | h8].
apply h5 in h7.
assumption.
apply h6 in h8.
assumption.
Qed.
