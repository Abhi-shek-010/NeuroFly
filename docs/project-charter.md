# NeuroFly Project Charter

## Purpose

NeuroFly is a connectome-constrained virtual adult fruit fly in a shared 3D experiment habitat. The first release is a narrow, inspectable taste-contact experiment that helps visitors see how measured circuit structure and explicit model choices can be connected to a predicted body response.

## Intended audience and setting

**Working proposal:** science learners and educators using a browser-based demonstration or exhibit, with judges and technical reviewers as a secondary audience. The intended setting is a desktop browser demonstration with a local exhibit fallback. The project owner still needs to confirm the primary audience, venue, target device, and browser.

## Primary research question

Can a neural model constrained by measured fly connections turn sensory events into coordinated actions that resemble published fly behavior, and do circuit perturbations change those actions in predicted ways?

## First visible behavior

When the fly makes valid physical contact with a taste patch, the modeled gustatory input and selected circuit may produce motor output that extends, holds, or retracts the proboscis. A trial with no response is also recorded and shown; the renderer does not force the expected action.

## Visitor role

The visitor selects or activates the defined taste stimulus, runs and observes the trial, and later compares a repeatable baseline with a declared neural intervention. The visitor does not directly pose or pilot the fly in a scientific trial. A separate developer-only pose control may be used for asset and actuator inspection and must be labeled as such.

## What success should communicate

After a baseline and a comparison run, a viewer should be able to follow stimulus contact, gustatory input, modeled circuit activity, motor output, and body response on one timeline. The viewer should also be able to distinguish measured wiring from modeled rules and predicted outcomes.

## Scope boundary

The first release covers taste contact to a feeding-related proboscis response only. Walking, food stopping, flight, odor search, visual escape, grooming, associative learning, and whole-brain behavior are deferred. The full biological cell path and final dataset release are not yet verified; those items remain explicit scientific gates.

## Working demo target

Desktop mouse and keyboard interaction on a recent laptop is the starting proposal. Chrome or Edge and an offline local fallback are proposed for the first review build. Exact browser, screen size, hardware, public hosting, and offline requirements remain owner decisions.

## Owner review

- Project owner: name to be recorded.
- Review date: 2026-11-08 proposed; confirm or replace.
- Charter status: proposed for Phase 0 review; not yet signed off.
