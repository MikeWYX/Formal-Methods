Lemma ex3: forall T (P: T -> Prop),
  (~ exists x, P x) -> forall x, ~ P x.
Proof.
intros.
intro h.
apply H.
exists x.
exact h.
Qed. 